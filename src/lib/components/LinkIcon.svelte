<script lang="ts">
	import type { IconLink } from "$lib";
	import Icon from "@iconify/svelte";

	export let target: string = "_blank";
	export let style: string = "";
	export let linkInfo: IconLink;
</script>

<a
	href={linkInfo.href}
	{target}
	aria-label={linkInfo.ariaLabel}
	class="hover:text-primary-400 hover:dark:text-primary-600"
>
	<Icon icon={linkInfo.icon} {style} />
</a>
