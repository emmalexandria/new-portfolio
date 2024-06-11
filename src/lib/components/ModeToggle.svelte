<script lang="ts">
    import { onMount } from "svelte";

	const storageKey: string = 'theme';
	let currentTheme: string = "light";

	const prefersDarkTheme = () => window.matchMedia('prefers-color-scheme: dark');

	onMount(() => {
		const stored = localStorage.getItem(storageKey);

		if(stored) {
			if(stored == "light" || stored == "dark") {

			currentTheme = stored;
			} else {
				localStorage.removeItem(storageKey)
			}
		}
	})

	const toggleTheme = () => {
		const stored = localStorage.getItem(storageKey);

		if (stored) {

		}
	}

</script>
<input type="checkbox" on:click={toggleTheme}/>