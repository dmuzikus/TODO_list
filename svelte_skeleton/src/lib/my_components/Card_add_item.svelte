<script>
    import Textfield from '@smui/textfield';
	import Select, { Option } from '@smui/select';
	import Snackbar from '@smui/snackbar';
	import List, { Item, Meta } from '@smui/list';
	import IconButton, { Icon } from '@smui/icon-button';
	let add_sub_display = 'flex'
    let add_subtask_value = ''
    export let store
    export let store_subtasks
    function addSubTask(value, current_id) {
		fetch('http://127.0.0.1:8000/api/add_sub?&value=' + value + '&id=' + current_id, {mode: 'no-cors'})
        store_subtasks.push(value)
	}
</script>
<Item selected={false} style="display: {add_sub_display}">
  <Textfield bind:value={add_subtask_value} label="Подзадача" style=""/>
    <Meta>
        <IconButton class="material-icons" on:click={()=>{addSubTask(add_subtask_value, store.id); store_subtasks = store_subtasks}}>add</IconButton>
    </Meta>
</Item>