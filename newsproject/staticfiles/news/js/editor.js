 let quill;
  document.addEventListener('DOMContentLoaded', () => {
    const toolbarOptions = [
      ['bold', 'italic', 'underline', 'strike'],
      [{ header: [1, 2, 3, false] }],
      [{ list: 'ordered' }, { list: 'bullet' }],
      [{ color: [] }, { background: [] }],
      [{ align: [] }],
      ['link', 'image', 'video'],
      ['clean']
    ];

    quill = new Quill('#quill-container', {
      theme: 'snow',
      modules: {
        toolbar: toolbarOptions
      }
    });

    const form = document.querySelector('form');
    const contentInput = document.querySelector('#content-input');

    form.addEventListener('submit', () => {
      contentInput.value = quill.root.innerHTML;
    });
  });