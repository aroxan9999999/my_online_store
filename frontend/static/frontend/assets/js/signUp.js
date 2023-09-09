var mix = {
	methods: {
		signUp () {
<<<<<<< HEAD
			const name = document.querySelector('#name').value
			const username = document.querySelector('#login').value
			const password = document.querySelector('#password').value
			this.postData('/api/sign-up', JSON.stringify({ name, username, password }))
				.then(({ data, status }) => {
					location.assign(`/`)
				})
				.catch(() => {
					alert('Ошибка авторизации!')
				})
=======
		    const name = document.querySelector('#name').value
            const username = document.querySelector('#login').value
			const password = document.querySelector('#password').value
			this.postData('/api/sign-up/', JSON.stringify({ name, username, password }))
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
<<<<<<< HEAD
}
=======
}
>>>>>>> 82db9917ac7303b4da9fe760dd8f324e84e0535a
