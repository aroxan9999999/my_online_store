var mix = {
	methods: {
		submitPayment() {
<<<<<<< HEAD
			const orderId = location.pathname.startsWith('/payment/')
				? Number(location.pathname.replace('/payment/', '').replace('/', ''))
				: null
			console.log({
				name: this.name,
				number: this.number1,
				year: this.year,
				month: this.month,
				code: this.code,
			})
			this.postData(`/api/payment/${orderId}`, {
				name: this.name,
				number: this.number1,
				year: this.year,
				month: this.month,
				code: this.code
			}).then(() => {
				alert('Успешная оплата')
				this.number1 = ''
				this.name = ''
				this.year = ''
				this.month = ''
				this.code = ''
				location.assign('/')
			}).catch(() => {
			 	console.warn('Ошибка при оплате')
			})
=======
			console.log('qweqwewqeqweqw')
			const orderId = location.pathname.startsWith('/payment/')
				? Number(location.pathname.replace('/payment/', '').replace('/', ''))
				: null
			this.postData(`/api/payment/${orderId}/`, {
				name: this.name,
				number: this.number,
				year: this.year,
				month: this.month,
				code: this.code
			})
				.then(() => {
					alert('Успешная оплата')
					this.number = ''
					this.name = ''
					this.year = ''
					this.month = ''
					this.code = ''
					location.assign('/')
				})
				.catch(() => {
					console.warn('Ошибка при оплате')
				})
>>>>>>> 82db9917ac7303b4da9fe760dd8f324e84e0535a
		}
	},
	data() {
		return {
<<<<<<< HEAD
			number1: '',
=======
			number: '',
>>>>>>> 82db9917ac7303b4da9fe760dd8f324e84e0535a
			month: '',
			year: '',
			name: '',
			code: ''
		}
	}
}