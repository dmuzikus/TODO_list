import cookie from 'cookie';
export const handle = async ({ request, resolve }) => {
	const cookies = cookie.parse(request.headers.cookie || '');
	request.locals.session_id = cookies.session_id

	// TODO https://github.com/sveltejs/kit/issues/1046
	if (request.query.has('_method')) {
		request.method = request.query.get('_method').toUpperCase();
	}

	if (request.locals.session_id || (request.path === '/auth/login'))
		return await resolve(request);
	else return {
		status: 301,
		headers: {
			location: 'auth/login'
		}
	}
};


export function getSession(request) {
	return request.locals.session_id ? {
		session_id: request.locals.session_id,
	} : {};
}