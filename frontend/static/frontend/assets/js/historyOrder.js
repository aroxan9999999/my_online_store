var mix = {
	methods: {
		getHistoryOrder() {
<<<<<<< HEAD
			this.getData("/api/orders")
=======
			this.getData("/api/orders/")
>>>>>>> 82db9917ac7303b4da9fe760dd8f324e84e0535a
				.then(data => {
					console.log(data)
					this.orders = data
				}).catch(() => {
				this.orders = []
				console.warn('Ошибка при получении списка заказов')
			})
		}
	},
	mounted() {
		this.getHistoryOrder();
	},
	data() {
		return {
			orders: [],
		}
	}
}