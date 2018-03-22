// bootstrap the demo
var baseUrl = "http://127.0.0.1:5000";
var demo = new Vue({
    el: '#demo',
    created: function () {
        //this.getClusters()
    },
    data: {
        clusters: [
            {
                name: "kafka",
                host_stat: [
                    {host: 'hs01', state: "active"},
                    {host: 'hs02', state: "active"},
                    {host: 'hs03', state: "active"}]
            },
            {
                name: "jstorm",
                host_stat: [
                    {host: 'hs04', state: "active"},
                    {host: 'hs05', state: "active"},
                    {host: 'hs06', state: "active"}]
            },
            {
                name: "redis",
                host_stat: [
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
                    console.log(data)
                },
                error: function () {
                    ins.gridData = [{host: 'hs02', state: "active"}]
                }
            });
        },
        change: function () {
            this.gridData = [{host: 'hahahahah', state: "active"}]
        }
    }
});
