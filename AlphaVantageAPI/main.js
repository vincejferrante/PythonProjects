const APIkey = "MY_API_KEY";

const netIncome = [];
const Revenue = []
fetch(`https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=IBM&apikey=${APIkey}`)
  .then(response => response.json())
  .then(data => {
    const netIncome = data.annualReports;
    const netIncomeTotals = netIncome.map(report => report.netIncome / 100000000);
    const Revenue = data.annualReports;
    const RevenueTotals = Revenue.map(report => report.totalRevenue / 100000000);
    console.log(netIncomeTotals, RevenueTotals);
    //console.log(data)
  })
  .catch(error => {
    console.log('Error:', error);
  });


