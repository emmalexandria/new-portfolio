<script lang="ts">
    export let onClick: Function;
</script>

<button on:click={onClick()} class="font-light font-display bg-primary-600 px-4 py-2 rounded-sm text-mono-50">
    <slot/>
</button>