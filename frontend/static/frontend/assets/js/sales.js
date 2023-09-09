var mix = {
    methods: {
        getSales(page = 1) {
<<<<<<< HEAD
            this.getData("/api/sales", {
=======
            this.getData("/api/sales/", {
>>>>>>> 82db9917ac7303b4da9fe760dd8f324e84e0535a
                currentPage: page,
            }).then(data => {
                this.salesCards = data.items
                this.currentPage = data.currentPage
                this.lastPage = data.lastPage
            })
        },
    },
    mounted() {
        this.getSales();
    },
    data() {
        return {
            salesCards: [],
            currentPage: 1,
            lastPage: 1,
            // TODO добавить пагинацию
        }
    },
}