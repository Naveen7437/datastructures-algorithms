let transactions = [ { id: 3, sourceAccount: 'A', targetAccount: 'B', amount: 100, category: 'eating_out', time: '2018-03-02T10:34:30.000Z' }, { id: 1, sourceAccount: 'A', targetAccount: 'B', amount: 100, category: 'eating_out', time: '2018-03-02T10:33:00.000Z' }, { id: 6, sourceAccount: 'A', targetAccount: 'C', amount: 250, category: 'other', time: '2018-03-02T10:33:05.000Z' }, { id: 4, sourceAccount: 'A', targetAccount: 'B', amount: 100, category: 'eating_out', time: '2018-03-02T10:36:00.000Z' }, { id: 2, sourceAccount: 'A', targetAccount: 'B', amount: 100, category: 'eating_out', time: '2018-03-02T10:33:50.000Z' }, { id: 5, sourceAccount: 'A', targetAccount: 'C', amount: 250, category: 'other', time: '2018-03-02T10:33:00.000Z' } ];


function findDuplicateTransactions(transactions = []) {
    let duplidateTransactions = [];
    let groupedTransactions = {};

    // creating groups on the basis of the given info
    transactions.forEach(t => {
        let key = t.sourceAccount + t.targetAccount + t.amount + t.category;
        if (groupedTransactions.hasOwnProperty(key)) {
            groupedTransactions[key].push(t);
        } else {
            groupedTransactions[key] = [t];
        }
    });

    // sorting the keys on the basis of time
    Object.keys(groupedTransactions).forEach(function (key, index) {
        groupedTransactions[key].sort((a, b) => (new Date(a.time) > new Date(b.time)) ? 1 : -1);
    });

    Object.keys(groupedTransactions).forEach(function (key, index) {
        // creating a small group of duplicate transactions
        let smallGroups = [groupedTransactions[key][0]];

        // start time of the fist transaction and 
        let starttime = groupedTransactions[key][0]['time'];

        // iterating over a group
        for (var i = 1; i < groupedTransactions[key].length; i++) {
            let datesDiff = new Date(groupedTransactions[key][i]['time']) - new Date(starttime);
            starttime = groupedTransactions[key][i]['time'];
            datesDiff = (datesDiff / 1000) / 60;

            // if the 
            if (datesDiff >=0 && datesDiff < 1) {
                smallGroups.push(groupedTransactions[key][i]);
            } else {
                if (smallGroups.length > 1) {
                    duplidateTransactions.push(smallGroups);
                }
                // creating a new small group if the above condition fails
                smallGroups = [groupedTransactions[key][i]];
            }
            // if its the last element, pushing it in duplicate transactions 
            if (i === groupedTransactions[key].length -1 && smallGroups.length > 1){
                duplidateTransactions.push(smallGroups);
            }

        }

    });
  
  return duplidateTransactions;
}

console.log(findDuplicateTransactions(transactions));


