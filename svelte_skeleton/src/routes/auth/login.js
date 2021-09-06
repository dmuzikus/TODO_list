import cookie from 'cookie';
import { user, setUser } from "/src/my_store";

export async function post(request) {
    console.log('in body')
    let login = request.body.get('login')
    let password = request.body.get('password')
    const django_fetch = await fetch('http://127.0.0.1:8000/api/auth_usr', {
        method: 'POST',
        headers: {
            'Authorization': 'Basic ' + encodeURI(login) + ' ' + encodeURI(password)
        },
    })
    const res = await django_fetch.json()
    console.log('RESULT OF DJANGO_FETCH')
    console.log(res)
    if (res['status']==='logged') {
        setUser(login)
        console.log(login)
        console.log(JSON.stringify(user))
        return {
            body: {'result': 'ok'},
            headers: {
                //'set-cookie': {'login': login, 'password': password}
                'set-cookie': [`session_id=${res['session_id']}; Path=/; HttpOnly`]
            }
        }
    }
    else {
        return {
        }
    }
}