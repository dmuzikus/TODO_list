<script>
	import '../app.css';
	import '../bare.css';
	import TopAppBar, {
    Row,
    Section,
    Title,
  } from '@smui/top-app-bar';
  import IconButton from '@smui/icon-button';
  import { goto, invalidate, prefetch, prefetchRoutes } from '$app/navigation';

  let variant = 'short';
  let collapsed = false;
  let topAppBar;

  async function logout_user() {
        await fetch('auth/logout', {
        	method: 'GET'
		})
	 	goto('/auth/login')
        }
</script>
<TopAppBar bind:this={topAppBar} {variant} bind:collapsed>
  <Row>
    <Section>
      <Title>ITMO.todo_list</Title>
    </Section>
    <Section align="end">
      <IconButton class="material-icons" aria-label="Download" on:click={logout_user}>logout</IconButton>
    </Section>
  </Row>
</TopAppBar>
<main>
	<slot />
</main>


<style>
	main {
		flex: 1;
		display: flex;
		flex-direction: column;
		padding: 1rem;
		width: 100%;
		max-width: 1024px;
		margin: 56px auto;
		box-sizing: border-box;
	}

	footer {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		padding: 40px;
	}

	footer a {
		font-weight: bold;
	}

	@media (min-width: 480px) {
		footer {
			padding: 40px 0;
		}
	}
</style>
