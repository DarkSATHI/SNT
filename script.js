import {
    data
}
from './data.js'
let app = Vue.createApp({
    data() {
        return {
            choix: 0,
            tableProjets: [1, 2, 3, 4, 5],
            projets: data
        }
    },
    created() {
        document.addEventListener('DOMContentLoaded', function () {
            let side = document.getElementById("mobile-demo")
            M.Sidenav.init(side)
        });
    },
    methods: {
        sideClose(indice) {
            this.choix = indice;
            let side = document.getElementById("mobile-demo")
            let instance = M.Sidenav.getInstance(side)
            instance.close();
            this.cardPresentationClose()
        },
        cardPresentationClose() {
            let side = document.getElementById("cardPresentation")
            side.style.display = "none"
        }
    }
})
app.mount('#app')