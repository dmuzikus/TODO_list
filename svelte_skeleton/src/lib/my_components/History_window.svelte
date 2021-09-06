<script>
  import Dialog, { Header, Title, Content, Actions } from '@smui/dialog';
  import IconButton from '@smui/icon-button';
  import Button, { Label } from '@smui/button';
  import List, { Item, Meta} from '@smui/list';
  export let deleted_store
  export let open;

</script>
<Dialog
  bind:open
  fullscreen
  aria-labelledby="fullscreen-title"
  aria-describedby="fullscreen-content"
>
  <Header>
    <Title id="fullscreen-title">История задач</Title>
    <IconButton action="close" class="material-icons">close</IconButton>
  </Header>
  <Content id="fullscreen-content">
    {#if deleted_store.length!==0}
      <List class="demo-list" checkList>
        {#each deleted_store as del_store}
          <Item>
            <Label>{del_store.title}</Label>
            <Meta>
              {del_store.group}
            </Meta>
          </Item>
        {/each}
      </List>
    {:else}
      Пусто
    {/if}
  </Content>
</Dialog>





