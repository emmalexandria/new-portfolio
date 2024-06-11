<script lang="ts">
    import { page } from "$app/stores";
    import H1 from "$lib/components/typography/H1.svelte";
    import H2 from "$lib/components/typography/H2.svelte";
    import P from "$lib/components/typography/P.svelte"
    import Icon from "@iconify/svelte"

    let message = $page.status >= 400 && $page.status <= 499 ? "Looks like this one is on you" : "Something went wrong on my end, sorry!"
</script>
<div class="w-fit mx-auto text-center">
    <span class="mx-auto block w-fit text-5xl md:text-9xl">
        <Icon icon="mdi:error"/>
    </span>
<H1>{$page.status}</H1>
<p class="text-3xl md:text-5xl mb-8">{$page.error?.message}</p>
<p class="font-body text-xl md:text-2xl">{message}</p>

</div>
