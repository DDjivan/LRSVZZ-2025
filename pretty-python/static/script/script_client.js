 function adjustQty(id, delta) {
      const input = document.getElementById('qty_' + id);
      const current = parseInt(input.value) || 0;
      const newValue = Math.max(0, current + delta);
      input.value = newValue;
    }
