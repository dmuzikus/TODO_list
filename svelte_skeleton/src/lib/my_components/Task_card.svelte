<script>
	import Card, {
		Content,
		PrimaryAction,
		Actions,
		ActionButtons,
		ActionIcons,
	} from '@smui/card';
	import Button, {Label} from '@smui/button';
	import IconButton, {Icon} from '@smui/icon-button';
	import Checkbox from '@smui/checkbox';
	import FormField from '@smui/form-field';
	import Textfield from '@smui/textfield';
	import Select, {Option} from '@smui/select';
	import Snackbar from '@smui/snackbar';
	import List, {Item, Meta} from '@smui/list';
	import Card_item from "$lib/my_components/Card_add_item.svelte"
	import Card_add_item from "./Card_add_item.svelte";


	function edit_item(index, title, current_id) {
		fetch('http://127.0.0.1:8000/api/change_field?field=title&value=' + title + '&id=' + current_id, {mode: 'no-cors'})
		console.log(index)
	}

	function delete_item(index, current_id) {
		fetch('http://127.0.0.1:8000/api/change_field?field=is_deleted&value=True&id=' + current_id, {mode: 'no-cors'})
		bd_store.splice(index, 1)
	}

	function handleCheckBox(box_value, current_id) {
		let edited_value
		switch (box_value) {
			case true:
				edited_value = 'True'
				break
			case false:
				edited_value = 'False'
				break
		}
		fetch('http://127.0.0.1:8000/api/change_field?field=is_finished&value=' + edited_value + '&id=' + current_id, {mode: 'no-cors'})
	}

	let checked = false
	let focused = false;


	export let store
	export let subtasks_store
	export let bd_store
	export let user
</script>

					<Card style="width: auto; min-width: 500px; max-width: 700px;margin-bottom: 10px">
						<Content>
							<FormField>
								<Checkbox bind:checked={store.is_finished} on:change={()=>{checked = store.is_finished; handleCheckBox(checked, store.id)}}/>
						  	</FormField>
							<Textfield textarea bind:value={store.title} label="Задача" style="width: 300px; margin-bottom: 15px"/>
							<span style="color: #018786">{store.group}</span>
							<List class="demo-list" checkList>
								<Card_add_item bind:store={store} bind:store_subtasks={subtasks_store}>
								</Card_add_item>
									{#key subtasks_store.length}
										{#each subtasks_store as subtask}
											<Item>
												<Label>{subtask}</Label>
												<Meta>
													<Checkbox value={subtask} />
												</Meta>
											</Item>
										{/each}
									{/key}
							  </List>
						</Content>
						<Actions style="align-items: center; justify-content: center;">
							<Button on:click={()=>{edit_item(bd_store.indexOf(store),store.title,store.id); bd_store = bd_store}}>
								<Label>Изменить</Label>
							</Button>
							<Button on:click={()=>{delete_item(bd_store.indexOf(store), store.id); bd_store = bd_store}}>
								<Label>Удалить</Label>
							</Button>
						</Actions>
					</Card>



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