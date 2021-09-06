/** @type {import('@sveltejs/kit').Config} */
const config = {
	kit: {
		target: '#svelte',
		vite: {
			ssr: {
				noExternal: ['@smui/*']
			},
		},
	}
};

export default config;
