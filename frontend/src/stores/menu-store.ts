import { create } from 'zustand';
import { Menu } from '@/types';
interface MenuState {
  currentMenu: Menu | null;
  shoppingList: IngredientAggregate[];
  exportFormat: 'csv' | 'excel' | 'pdf';
  setExportFormat: (format: 'csv' | 'excel' | 'pdf') => void;
  fetchShoppingList: (menuId: number) => Promise<void>;
  exportShoppingList: () => Promise<void>;
}

export const useMenuStore = create<MenuState>((set) => ({
  currentMenu: null,
  shoppingList: [],
  exportFormat: 'csv',
  setExportFormat: (format) => set({ exportFormat: format }),
  fetchShoppingList: async (menuId) => {
    const response = await axios.get(`/api/v1/menus/${menuId}/shopping-list`);
    set({ shoppingList: response.data });
  },
  exportShoppingList: async () => {
    const { exportFormat, currentMenu } = get();
    const response = await axios.get(
      `/api/v1/menus/${currentMenu.id}/export?format=${exportFormat}`,
      { responseType: 'blob' }
    );
    // Trigger browser download
    const url = window.URL.createObjectURL(new Blob([response.data]));
    const link = document.createElement('a');
    link.href = url;
    link.setAttribute('download', `shopping_list.${exportFormat}`);
    document.body.appendChild(link);
    link.click();
  },
}));