<script lang="ts">
    import { page } from "$app/stores";
    import { onMount } from "svelte";

    export let href: string;
    export let title: string;

</script>

 <li class="font-display font-light hover:font-normal transition-all" >
    <a {href}>
        <p class={$page.url.pathname == href ? "font-bold transition-all" : "transition-all"}>
            {title}
        </p>
     </a>
</li>   
