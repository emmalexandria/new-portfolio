<script>
    import H1 from "$lib/components/typography/H1.svelte";
    import H2 from "$lib/components/typography/H2.svelte";
    import P from "$lib/components/typography/P.svelte";
</script>

<svelte:head>
    <title>About me</title>
    <meta name="description" content="Information about me" />
</svelte:head>

<div class="flex flex-col md:flex-row gap-8">
    <img src="/me2.webp" alt="Me standing by windows" class="md:hidden" />
    <div class="md:mr-16">
        <div>
            <H1>About me</H1>

            <P>
                My name is Emma Alexandria. I’m a software developer from Cape
                Town with a particular interest in web development, web design,
                and terminal tooling. I particularly enjoy the feeling of
                finishing a project. There’s little more satisfying to me than
                putting out a completed code base with a title, logo, and
                detailed usage documentation. I’m passionate about web
                accessibility standards and the development of an open and safe
                internet. I’ve had an interest in the technical complexities of
                computing from a very young age. I see computers as an essential
                engine for human progress and perhaps in time the most
                significant invention humanity has produced. I also enjoy formal
                writing and typesetting documents.
            </P>
        </div>
        <div class="flex flex-col md:flex-row gap-8">
            <div class="md:w-3/5">
                <H2>Skills</H2>
                <P>
                    My main skills lie in web development, particularly with
                    Svelte, Typescript, and Tailwind. However, I also have
                    significant experience with Rust, and some experience with
                    C#, Java, Go, and Python. Further, I have some basic
                    experience with data visualization and graphics development.
                    I have a strong basis in the fundamentals of computing, and
                    I am a proficient Linux user. My most significant asset is
                    that when it comes to computers I’m an extremely fast and
                    intuitive learner. I’m also a regular user of the Adobe
                    suite, DaVinci Resolve, and LaTex.
                </P>
            </div>
            <div class="md:w-2/5">
                <H2>Interests</H2>
                <P>
                    In my free time I enjoy editing Wikipedia, creating and
                    typesetting personal writing, listening to albums, and
                    writing code. I think I enjoy them due to my prior mentioned
                    enjoyment of the complete works.These things are
                    opportunities to judge the cohesivenss and clarity of
                    something in communicating ideas.
                </P>
            </div>
        </div>
    </div>
    <img
        src="me.webp"
        width="881"
        height="1791"
        class="h-screen hidden md:block"
        alt="Me standing by some windows"
    />
</div>
