// from data.js
var tableData = data;
var tbody = d3.select("tbody");

function TableRows(data) {
tbody.html("");
data.forEach( function(fillRow){
    //console.log(fillRow);
    // Use d3 to append one table row `tr` for each object
    

    var row =tbody.append("tr");
// Use `Object.entries` to console.log each value
    Object.entries(fillRow).forEach( function([key, value]){
        //console.log(key, value);
        row.append("td").text(value);
        });
});
}

d3.selectAll("#filter-btn").on("click",function(ButtonSearch) {
    d3.event.preventDefault();
    var selectDate = d3.select("#datetime").property("value");
    filterData = tableData.filter(row => row.datetime === selectDate);
    TableRows(filterData);
    //console.log(selectDate);
    return false;
});

TableRows(data)