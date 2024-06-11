<script lang="ts">
    import Icon from "@iconify/svelte";

	export let href: string;
	export let target: string = "_blank";
	export let icon: string;
	export let style: string = "";
</script>

<a {href} {target} class="hover:text-primary-400 hover:dark:text-primary-600">
	<Icon {icon} {style}/>
</a>