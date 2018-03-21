// bootstrap the demo
var baseUrl = "http://127.0.0.1:5000";
var demo = new Vue({
    el: '#demo',
    created: function () {
        //this.getClusters()
    },
    data: {
        searchQuery: '',
        gridColumns: ['host', 'state'],
        gridData: [
            {host: 'hs01', state: "active"},
            {host: 'hs02', state: "active"},
            {host: 'hs03', state: "active"}
        ]
    },
    methods: {
        getClusters: function () {
            ins = this;
            return $.ajax({
                type: 'get',
                url: baseUrl+'/getComps',
                data: {},
                //cache: false,
                //dataType: 'json',
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
