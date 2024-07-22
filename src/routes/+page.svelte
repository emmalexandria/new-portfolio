<script>
    import H2 from "$lib/components/typography/H2.svelte";
    import ProjectCard from "$lib/components/ProjectCard.svelte";
    import H1 from "$lib/components/typography/H1.svelte";
    import ProjectSection from "$lib/components/ProjectSection.svelte";
    import P from "$lib/components/typography/P.svelte";
    import { error } from "@sveltejs/kit";
    import EmphLink from "$lib/components/EmphLink.svelte";
    import Icon from "@iconify/svelte";
</script>

<svelte:head>
    <title>Emma Alexandria's Portfolio</title>
    <meta
        name="description"
        content="The personal portfolio of Emma Alexandria"
    />
</svelte:head>

<section class="h-[80vh]">
    <div
        class="flex flex-col w-full md:w-1/2 gap-4 mx-auto items-center justify-center text-center mt-8 md:mt-16"
    >
        <H1>Web and software developer</H1>
        <P
            >I work in web and software development. I also have experience in
            web design, writing, typesetting, and digital content creation.</P
        >
        <EmphLink href="#portfolio" target="_self"
            ><span class="flex flex-row items-center gap-2"
                ><Icon icon="mdi:arrow-down" />Portfolio</span
            ></EmphLink
        >
    </div>
</section>

<section class="pb-8 w-full md:w-3/4 mx-auto">
    <H1 id="portfolio">Portfolio</H1>
    <div class="w-full">
        <P>
            The following is a sampling of projects of mine that I consider
            finished or currently active. I have built much more than this,
            however most ended up being shuttered or replaced.
        </P>
    </div>

    <ProjectSection title="Web">
        <ProjectCard
            title="M3 Tailwind"
            links={[
                {
                    href: "https://m3tw.emmalexandria.dev",
                    icon: "mdi:link-variant",
                    ariaLabel: "Check out the Material Tailwind generator",
                },
                {
                    href: "https://github.com/emmalexandria/material-tailwind",
                    icon: "mdi:github",
                    ariaLabel:
                        "Look at the source code of the Material Tailwind generator",
                },
            ]}
            tech={["devicon-plain:svelte", "mdi:tailwind"]}
            >Utility for generating a Material Design color palette and
            exporting it to the Tailwind CSS config format. Built with Material
            components and changes colour according to the generated color
            scheme.
        </ProjectCard>
        <ProjectCard
            title="Hugo blog"
            links={[
                {
                    href: "https://blog.emmalexandria.dev",
                    icon: "mdi:link-variant",
                    ariaLabel: "Read my blog here",
                },
                {
                    href: "https://github.com/emmalexandria/hugo-blog",
                    icon: "mdi:github",
                    ariaLabel: "Look at my blog's source code",
                },
            ]}
            tech={["devicon-plain:hugo"]}
            >Personal blog built with Hugo. Refactored and modified large
            amounts of HTML and CSS from another theme and set up multiple blog
            sections.</ProjectCard
        >
    </ProjectSection>
    <ProjectSection title="Terminal">
        <ProjectCard
            title="rrecycle"
            links={[
                {
                    href: "https://github.com/emmalexandria/rrecycle",
                    icon: "mdi:github",
                    ariaLabel: "Look at the source code of rrecycle",
                },
            ]}
            tech={["devicon-plain:rust"]}
            >Cross-platform file deletion utility with support for recycle bin
            and secure deletion through file overwrites.</ProjectCard
        >
        <ProjectCard
            title="fRCON"
            links={[
                {
                    href: "https://github.com/emmalexandria/frcon",
                    icon: "mdi:github",
                    ariaLabel: "Look at the source code of fRCON",
                },
            ]}
            tech={["devicon-plain:rust"]}
            >RCON client with command completion and formatting for both error
            and success responses.</ProjectCard
        >
        <ProjectCard
            title="optimg"
            links={[
                {
                    href: "https://github.com/emmalexandria/optimg",
                    icon: "mdi:github",
                    ariaLabel: "Look at the source code of fRCON",
                },
            ]}
            tech={["simple-icons:go"]}
            >Image resizing utility built for web development with the goal of
            creating images to be used in srcset.</ProjectCard
        >
    </ProjectSection>
</section>
