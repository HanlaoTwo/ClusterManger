/**
 * Created by hanqian18790 on 2018/3/22.
 * .
 */
Vue.component('cluster', {
    template: '#cluster-template',
    //replace: true,
    props: ['ci'],
    data: function () {
        return {
                host_stata: [
                    {host: 'hs01', state: "active"},
                    {host: 'hs02', state: "active"},
                    {host: 'hs03', state: "active"}]
        }
    },

    methods: {
        fresh: function (key) {
            console.log("hahahahahhahaha")
        },
        stop: function (key) {
            this.host_stata = [{host: 'hs02', state: "active"}]
        },
        start: function (key) {
            this.clusterinfo.host_stata = [{host: 'hs03', state: "active"}]
        },
        restart: function (key) {
            this.clusterinfo.host_stata = [{host: 'hs04', state: "active"}]
        }
    }
});
