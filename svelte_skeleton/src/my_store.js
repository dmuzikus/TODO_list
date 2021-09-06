import {writable} from "svelte/store";
export let user = writable('')
export let current_user = null
export function setUser(value) {
    current_user = value
}