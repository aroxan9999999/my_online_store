var mix = {
	methods: {
		getBanners() {
			this.getData("/api/banners")
				.then(data => {
					this.banners = data
				}).catch(() => {
				this.banners = []
				console.warn('Ошибка при получении баннеров')
			})
		},
		getPopularProducts() {
<<<<<<< HEAD
			this.getData("/api/products/popular")
=======
			this.getData("/api/products/popular/")
>>>>>>> 82db9917ac7303b4da9fe760dd8f324e84e0535a
				.then(data => {
					this.popularCards = data
				})
				.catch((error) => {
					console.log('----', error)
					this.popularCards = []
					console.warn('Ошибка при получении списка популярных товаров')
				})
		},
		getLimitedProducts() {
<<<<<<< HEAD
			this.getData("/api/products/limited")
=======
			this.getData("/api/products/limited/")
>>>>>>> 82db9917ac7303b4da9fe760dd8f324e84e0535a
				.then(data => {
					this.limitedCards = data
				}).catch(() => {
				this.limitedCards = []
				console.warn('Ошибка при получении списка лимитированных товаров')
			})
		},
	},
	mounted() {
		this.getBanners();
		this.getPopularProducts();
		this.getLimitedProducts();
	},
   created() {
     this.getLimitedProducts()
   },
	data() {
		return {
			banners: [],
			popularCards: [],
			limitedCards: [],
		}
	}
}