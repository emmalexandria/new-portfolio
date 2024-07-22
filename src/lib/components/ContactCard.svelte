<script lang="ts">
	import Icon from "@iconify/svelte";

	export let href: string;
	export let icon: string = "";
</script>

<a
	{href}
	class="block bg-mono-100 dark:bg-mono-800 rounded-sm hover-shadow px-4 py-2 w-fit text-sm md:text-base"
	target="_blank"
>
	<div class="flex flex-row items-center gap-2">
		<Icon {icon} inline={true} />
		<p>
			<slot />
		</p>
	</div>
</a>

