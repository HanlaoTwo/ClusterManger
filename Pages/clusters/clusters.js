// bootstrap the demo
var baseUrl = "http://127.0.0.1:5000";
var demo = new Vue({
    el: '#demo',
    created: function () {
        //this.getClusters()
    },
    data: {
        clusters:["1","2"],
        clusters0: [
            {
                name: "kafka",
                host_stata: [
                    {host: 'hs01', state: "active"},
                    {host: 'hs02', state: "active"},
                    {host: 'hs03', state: "active"}]
            },
            {
                name: "jstorm",
                host_stata: [
                    {host: 'hs04', state: "active"},
                    {host: 'hs05', state: "active"},
                    {host: 'hs06', state: "active"}]
            },
            {
                name: "redis",
                host_stata: [
                    {host: 'hs07', state: "active"},
                    {host: 'hs08', state: "active"},
                    {host: 'hs09', state: "active"}]
            }],
        gridColumns: ['host', 'state'],
        gridData: []
    },
    methods: {
        getClusters: function () {
            ins = this;
            return $.ajax({
                type: 'get',
                url: baseUrl + '/getComps',
                data: {},
                success: function (data) {
                    console.log(data);
                    ins.clusters = setClusters(data);
                    console.log(ins.clusters)
                },
                error: function () {
                    //do something
                }
            });
        }

    }

});
function setClusters (data) {
    var clusters = JSON.parse(data);
    var names =[];
    for(name in clusters) {
        names.push(name);
    }
    return names;
}