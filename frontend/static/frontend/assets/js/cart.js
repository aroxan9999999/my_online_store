var mix = {
    methods: {
        submitBasket () {
<<<<<<< HEAD
            this.postData('/api/orders', Object.values(this.basket))
=======
            this.postData('/api/orders/', Object.values(this.basket))
>>>>>>> 82db9917ac7303b4da9fe760dd8f324e84e0535a
                .then(({data: { orderId }}) => {
                    location.assign(`/orders/${orderId}/`)
                }).catch(() => {
                    console.warn('Ошибка при создании заказа')
                })
        }
    },
    mounted() {},
    data() {
        return {}
    }
<<<<<<< HEAD
}
=======
}
>>>>>>> 82db9917ac7303b4da9fe760dd8f324e84e0535a
