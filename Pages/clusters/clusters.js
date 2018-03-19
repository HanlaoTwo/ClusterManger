// bootstrap the demo
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
                url: '/hello',
                data: {},
                cache: false,
                dataType: 'json',
                success: function (data) {
                    gridData = data
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
