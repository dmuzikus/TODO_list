<script context="module">
    export async function load({ page, fetch, session, context }) {
        return {
            status: 200
        }
    }
</script>

<script>
    import Textfield from '@smui/textfield';
    import HelperText from '@smui/textfield/helper-text';
    import Card, { Actions, Content } from '@smui/card';
    import Button, { Label } from '@smui/button';
    import Snackbar from '@smui/snackbar';
    import { goto, invalidate, prefetch, prefetchRoutes } from '$app/navigation';

    let snackbarWithClose;
    let entry_error;
    let login_value = "";
    let password_value = null;
    let login_field;
    let password_field;
    let is_invalid = false;
    let is_invalid2 = false;

    async function validation_user() {
        let My_form  = new FormData()
        My_form.append('login', login_value)
        My_form.append('password', password_value)
        console.log('Send post')
        const res = await fetch('/auth/login', {
            method: 'POST',
            body: My_form
        })
        console.log('Sended post')
        const json = await res.json()
        console.log(json)
        if (res.ok && json['result'] === 'ok') {
            goto('/')
        } else {
            entry_error.open()
        }
    }

    function send_validated_data() {
        if (login_value&&password_value) {validation_user()}
        else {login_handler(login_value); password_handler(password_value); snackbarWithClose.open()}
    }

    function login_handler(value) {
        is_invalid = !value
    }

    function password_handler(value) {
        is_invalid2 = !value
    }
</script>

<div class="outer" style="height:100%; width: 100%">
    <span class="inner">
        <div class="card-container" style="width: 310px;">
            <Card>
                <Content>
                    <div class="margins">
                        <Textfield bind:this={login_field} updateInvalid={false} invalid={is_invalid}
                                   bind:value={login_value} label="Login" on:change={()=>{if (login_value) is_invalid=false}}>
                            <HelperText validationMsg slot="helper">
                                That's not a valid login.
                            </HelperText>
                        </Textfield>
                        <Textfield bind:this={password_field} type="password" updateInvalid={false} invalid={is_invalid2}
                                   bind:value={password_value} label="Password" on:change={()=>{if (password_value) is_invalid2=false}}>
                            <HelperText validationMsg slot="helper">
                                That's not a valid password.
                            </HelperText>
                        </Textfield>
                    </div>
                </Content>
                    <Actions style="justify-content: center; margin-bottom: 10px;">
                        <Button on:click={() => send_validated_data()} variant="raised">
                            <Label>Login</Label>
                        </Button>
                    </Actions>
            </Card>
            <Snackbar bind:this={snackbarWithClose}>
                <Label>Заполните все поля</Label>
            </Snackbar>
        </div>
    </span>
</div>

<Snackbar bind:this={entry_error}>
    <Label>Ошибка входа</Label>
</Snackbar>

<!-- DEFAULT SLOT issue -->
{#if false}<slot/>{/if}

<style>
    .outer:before {
            content: '';
            display: inline-block;
            height: 100%;
            vertical-align: middle;
        }

    .inner {
        display: inline-block;
        vertical-align: middle;
    }

    .outer {
        text-align: center;
    }
</style>
