export async function get({ params }) {
    console.log('logout')
    console.log(params)
    return {
        status: 200,
        body: {'result': Date.now()},
        headers: {
            'set-cookie': `session_id=; path=/; HttpOnly`
        },
    }
}