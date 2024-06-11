<script lang="ts">
    export let href: string;
    export let target = "_blank";
</script>

<a {href} {target} class="font-light font-display bg-primary-600 px-4 py-2 rounded-sm text-mono-50">
    <slot/>
</a>