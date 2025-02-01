const getUsers = async () => {
    try {
        const response = await fetch('http://localhost:5000/users')
        
        if (!response.ok) {
            return null
        }

        return response.json()
    } catch (error) {
        return null
    }
}

const renderUsers = (users) => {
    const usersList = document.getElementById('usersList')
    usersList.innerHTML = ''

    users.forEach((user) => {
        const li = document.createElement('li')
        li.innerText = `${user.id}: ${user.name}`
        usersList.appendChild(li)
    })
}

const refreshUsers = async () => {
    const users = await getUsers()
    if (users) {
        renderUsers(users)
    }
}

const createUser = async (user) => {
    try {
        const response = await fetch(
            'http://localhost:5000/users',
            {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(user)
            }
        )
        if (!response.ok) {
            return null
        }
        return response.json()
    } catch (error) {
        return null
    }
}

const handleSubmit = async () => {
    const name = document.getElementById('name')
    const email = document.getElementById('email')

    const user = {
        name: name.value,
        email: email.value
    }
    const userCreated = await createUser(user)
    if (userCreated) {
        name.value = ''
        email.value = ''
        await refreshUsers()
        alert("Usuario creado correctamente")
    }
}

const main = async () => {
    await refreshUsers()

    const createUserBtn = document.getElementById('createUserBtn')
    createUserBtn.addEventListener('click', handleSubmit)
}

main()