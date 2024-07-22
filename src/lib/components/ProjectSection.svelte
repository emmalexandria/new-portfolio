<script lang="ts">
    import H2 from "./typography/H2.svelte";
    export let title: string;
</script>

<div class="mb-32 mt-16">
    <H2>{title}</H2>
    <div class="grid grid-flow-row md:grid-flow-col md:auto-cols-fr gap-8 mt-8">
        <slot />
    </div>
</div>
