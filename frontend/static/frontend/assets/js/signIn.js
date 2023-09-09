var mix = {
	methods: {
		signIn () {
			const username = document.querySelector('#login').value
			const password = document.querySelector('#password').value
<<<<<<< HEAD
			this.postData('/api/sign-in', JSON.stringify({ username, password }))
				.then(({ data, status }) => {
					location.assign(`/`)
				})
				.catch(() => {
					alert('Ошибка авторизации!')
				})
=======
			this.postData('/api/sign-in/', JSON.stringify({ username, password }))
				.then(({ data, status }) => {
					location.assign(`/`)
				})
>>>>>>> 82db9917ac7303b4da9fe760dd8f324e84e0535a
		}
	},
	mounted() {
	},
	data() {
		return {}
	}
}