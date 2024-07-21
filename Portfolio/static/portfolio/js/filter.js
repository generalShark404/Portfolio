function filterProjects(tag) {
    let projectContainers = document.querySelectorAll('.project-container');
    let noProject = document.querySelector('.no-project');

    projectContainers.forEach(container => {
        let tags = container.querySelector('.technology-tags').textContent.split(',').map(tag => tag.trim().toLowerCase());
        
        if (tag === '' || tags.includes(tag.toLowerCase())) {
            container.classList.remove('d-none');
            noProject.classList.add('d-none');
        } else {
            container.classList.add('d-none');
            noProject.classList.remove('d-none');
        }
    });
}