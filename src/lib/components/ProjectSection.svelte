<script lang="ts">
    import H2 from "./typography/H2.svelte";
    export let title: string; 
</script>
<div class="mb-32 mt-16i">
    
<H2>{title}</H2>
<div class="grid sm:grid-rows-3 md:grid-cols-3 md:grid-rows-none gap-16 mt-8">
<slot/>
</div>
    
</div>