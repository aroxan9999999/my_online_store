var mix = {
    methods: {
        getProfile() {
<<<<<<< HEAD
            this.getData(`/api/profile`).then(data => {
=======
            this.getData(`/api/profile/`).then(data => {
>>>>>>> 82db9917ac7303b4da9fe760dd8f324e84e0535a
                this.fullName = data.fullName
                this.avatar = data.avatar
                this.phone = data.phone
                this.email = data.email
            }).catch(() => {
                console.warn('Ошибка при получении профиля')
            })
        },
        changeProfile () {
            if(!this.fullName.trim().length || !this.phone.trim().length || !this.email.trim().length) {
                alert('В форме присутствуют незаполненные поля')
                return
            }

<<<<<<< HEAD
            this.postData('/api/profile', {
=======
            this.postData('/api/profile/', {
>>>>>>> 82db9917ac7303b4da9fe760dd8f324e84e0535a
                fullName: this.fullName,
                avatar: this.avatar,
                phone: this.phone,
                email: this.email
            }).then(({data}) => {
                this.fullName = data.fullName
                this.avatar = data.avatar
                this.phone = data.phone
                this.email = data.email
               alert('Успешно сохранено')
            }).catch(() => {
                console.warn('Ошибка при обновлении профиля')
            })
        },
        changePassword () {
            if (
                !this.passwordCurrent.trim().length ||
                !this.password.trim().length ||
                !this.passwordReply.trim().length ||
                this.password !== this.passwordReply
            ) {
                alert('В форме присутствуют незаполненные поля или пароли не совпадают')
                return
            }
<<<<<<< HEAD
            console.log({ currentPassword: this.passwordCurrent, newPassword: this.password })
            this.postData('/api/profile/password', { currentPassword: this.passwordCurrent, newPassword: this.password })
=======
            this.postData('/api/profile/password/')
>>>>>>> 82db9917ac7303b4da9fe760dd8f324e84e0535a
              .then(({data}) => {
                   alert('Успешно сохранено')
                    this.passwordCurrent = ''
                    this.password = ''
                    this.passwordReply = ''
                }).catch(() => {
                    console.warn('Ошибка при сохранении пароля')
                })
        },
        setAvatar (event) {
            const target = event.target
<<<<<<< HEAD
            const file = target.files[0]
=======
            const file = target.files?.[0] ?? null
>>>>>>> 82db9917ac7303b4da9fe760dd8f324e84e0535a
            if (!file) return

            const formData = new FormData()
            formData.append('avatar', file)

<<<<<<< HEAD
            this.postData('/api/profile/avatar', formData, {'Content-Type': 'multipart/form-data'})
            .then(() => {
                this.getProfile()
=======
            this.postData('/api/profile/avatar/', formData, {'Content-Type': 'multipart/form-data'}).then((data) => {
                this.avatar = data.url
>>>>>>> 82db9917ac7303b4da9fe760dd8f324e84e0535a
            }).catch(() => {
                 console.warn('Ошибка при обновлении изображения')
            })
        },
        getCookie(name) {
            let cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');
                for (let i = 0; i < cookies.length; i++) {
                    const cookie = cookies[i].trim();
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        },
        clearAvatar() {
            this.avatar = null
        }
    },
    created() {
        this.getProfile();
    },
    data() {
        return {
            fullName: null,
            phone: null,
            email: null,
            avatar: null,
            password: '',
            passwordCurrent: '',
            passwordReply: ''
        }
    },
}