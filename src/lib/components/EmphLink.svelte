<script lang="ts">
    export let href: string;
    export let target = "_blank";
</script>

<a
    {href}
    {target}
    class="font-light font-display border-2 border-primary-600 shadow-md shadow-primary-300 dark:shadow-primary-800 hover:bg-primary-600 px-4 py-2 rounded-sm hover:text-mono-50"
>
    <slot />
</a>
