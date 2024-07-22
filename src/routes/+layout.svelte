<script lang="ts">
    import "@fontsource-variable/roboto-slab";
    import "@fontsource-variable/montserrat";

    import Navigation from "$lib/components/Navigation.svelte";
    import "../app.css";
</script>

<header>
    <Navigation />
</header>
<main class="px-8 pt-8 md:px-16">
    <slot />
</main>
<footer></footer>
