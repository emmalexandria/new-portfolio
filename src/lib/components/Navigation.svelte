<script lang="ts">
    import Icon from "@iconify/svelte";
    import EmphLink from "./EmphLink.svelte";
    import NavItem from "./NavItem.svelte";
    import { quintOut } from "svelte/easing";
    import { slide } from "svelte/transition";
    import MobileNav from "./MobileNav.svelte";
    import DesktopNav from "./DesktopNav.svelte";

    let navOpen: boolean = false;
</script>

<div>
    <div class="flex flex-row mb-4 md:mb-none px-8 pt-8 md:px-16 md:pt-8">
        <a class="mr-auto font-display font-bold w-fit" href="/">
            <h1 class=" font-bold w-fit">Emma Alexandria</h1>
        </a>
        <button
            aria-label="Open navigation"
            type="button"
            class="block md:hidden"
            on:click={() => {
                navOpen = !navOpen;
            }}><Icon icon="mdi:menu" /></button
        >
        <DesktopNav />
    </div>

    {#if navOpen}
        <MobileNav />
    {/if}
</div>
