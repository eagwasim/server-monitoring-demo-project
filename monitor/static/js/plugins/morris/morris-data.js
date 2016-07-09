// Morris.js Charts sample data for SB Admin template

function loadData(){
    var url = "/monitor/json/load/serverdata";
    $.ajax({
        type : 'GET',
        url : url,
        dataType : 'json',
        success : function(data){
            populateData(data);
        },
        error : function(data){
            alert('An error occured while trying to load your data, please contact Emmanuel Agwasim.');
        }
    });
}

function populateData(payload){
    for(var index = 0 ; index < payload.length ; index++){
         Morris.Area({
             element: payload[index].elementName,
             data: payload[index].data,
             xkey: 'time',
             ykeys: ['network_speed','cpu_load','cpu_usage','free_ram'],
             labels: ['Network Speed','Average Load','CPU Usage','Free RAM'],
             pointSize: 2,
             hideHover: false ,
             resize: true,
             parseTime : false
         });
    }
}