//fetched_data = fetch('http://127.0.0.1:8000/', { mode: 'no-cors' }).then((response)=>response.json()).then((res)=>res);
async function getdata() {
    var data = await fetch(
        'http://127.0.0.1:8000/tasks', { mode: 'no-cors' }
    )
    const json = await data.json();
    return json;
}

var app = new Vue({
    el: '#app',
    data: {
        'tasks': 'Loading...',
    },
    methods: {
        renderlist() {
            getdata().then((a) => {
                app.tasks = a;
            });
        },

    },
    mounted() {
        this.renderlist();
    }
})