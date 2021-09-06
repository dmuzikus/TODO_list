<script context="module">
	let loaded = false
	export async function load({ page, fetch, session, context }) {
		console.log('Fetching to source')
		const bd_fetch_user = await fetch('http://127.0.0.1:8000/api/get_user?session_id='+session.session_id, {mode: 'no-cors'})
		const user_result = await bd_fetch_user.json()
		if (bd_fetch_user.ok) {
			const bd_fetch = await fetch('http://127.0.0.1:8000/api/get_tasks?user='+user_result['data'], {mode: 'no-cors'})
			const result = await bd_fetch.json()
			const bd_fetch2 = await fetch('http://127.0.0.1:8000/api/get_history?user='+user_result['data'], {mode: 'no-cors'})
			const result2 = await bd_fetch2.json()
			if (bd_fetch.ok) {
				loaded = true
		  		console.log('Got response')
		  		return {
				props: {
					bd_store: await result['data'],
					user: await user_result['data'],
					deleted_store: await result2['data']
				}
				}
			}
		}
		return {}
  }
</script>

<script>
	import Card, {
    Content,
    PrimaryAction,
    Actions,
    ActionButtons,
    ActionIcons,
  	} from '@smui/card';
  	import Button, { Label } from '@smui/button';
  	import IconButton, { Icon } from '@smui/icon-button';
	import Checkbox from '@smui/checkbox';
	import FormField from '@smui/form-field';
	import Textfield from '@smui/textfield';
	import Select, { Option } from '@smui/select';
	import Snackbar from '@smui/snackbar';
	import List, { Item, Meta } from '@smui/list';
	import Task_card from "$lib/my_components/Task_card.svelte"
	import History_window from "$lib/my_components/History_window.svelte"

  	let selected = ['Subtask1'];

  	let snackbarWithClose;
  	let groups = ['Day','Free time', 'Food', 'Sport','Somethings','Work'];
  	let select_value;

	export let bd_store = []
	export let deleted_store = []
	export let user

	function getSubtasksStore(row) {
		if (row) {
			if (row.includes(',')) return row.split(',').slice(0, -1)
		}
		else return []
	}

	function add_item(item) {
		console.log(select_value)
		if (item!=='') {
			console.log(item)
			fetch('http://127.0.0.1:8000/api/create_task?group='+select_value+'&title='+item+'&user='+user, {mode: 'no-cors'})
			bd_store.push({title: item, group: select_value})
			add_value = ''
			select_value = ''
		}
		else {snackbarWithClose.open()}
	}

	let add_value = ''
	let checked = false
	let focused = false;
	let my_open = false

</script>

<Snackbar bind:this={snackbarWithClose}>
  <Label>Заполните оба поля!</Label>
  <Actions>
    <IconButton class="material-icons" title="Dismiss">close</IconButton>
  </Actions>
</Snackbar>

<History_window bind:open={my_open} bind:deleted_store={deleted_store}>
</History_window>

<div style="margin: 15px auto; display: flex">
	<Textfield
		updateInvalid
		bind:value={add_value}
		label="Введите задачу..."
		style="min-width: 250px; margin-right: 15px"
		on:focus={() => (focused = true)}
		on:blur={() => (focused = false)}>
    </Textfield>
	<Select bind:value={select_value} label="Укажите группу">
      {#each groups as group}
        <Option value={group}>{group}</Option>
      {/each}
    </Select>
	<IconButton class="material-icons" on:click={()=>{add_item(add_value); bd_store = bd_store}}>add</IconButton>
	<IconButton class="material-icons" on:click={()=>{my_open=true}}>history</IconButton>
</div>

<section>
		<div class="card-container" style="flex-direction: column;">
			{#if bd_store}
				{#key bd_store.length||bd_store.values()}
					{#each bd_store as store}
						<Task_card bind:store={store} bind:user={user} subtasks_store={getSubtasksStore(store.subtasks)} bind:bd_store={bd_store}>
						</Task_card>
					{/each}
				{/key}
			{/if}
		</div>
</section>


<style>
	section {
		display: flex;
		justify-content: center;
		flex: 1;
	}

	h1 {
		width: 100%;
	}
	* :global(.shaped-outlined
      .mdc-notched-outline
      .mdc-notched-outline__leading) {
    border-radius: 28px 0 0 28px;
    width: 28px;
  }
  * :global(.shaped-outlined
      .mdc-notched-outline
      .mdc-notched-outline__trailing) {
    border-radius: 0 28px 28px 0;
  }
  * :global(.shaped-outlined .mdc-notched-outline .mdc-notched-outline__notch) {
    max-width: calc(100% - 28px * 2);
  }
  * :global(.shaped-outlined.mdc-text-field--with-leading-icon:not(.mdc-text-field--label-floating)
      .mdc-floating-label) {
    left: 16px;
  }
  * :global(.shaped-outlined + .mdc-text-field-helper-line) {
    padding-left: 32px;
    padding-right: 28px;
  }
   * :global(.demo-list) {
    max-width: 600px;
    border: 1px solid
      var(--mdc-theme-text-hint-on-background, rgba(0, 0, 0, 0.1));
  }
</style>
