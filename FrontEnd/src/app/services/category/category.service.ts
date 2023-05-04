import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import { CategoryBack, Product,  SubCategoryBack} from "../../models";
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class CategoryService {

  BASE_URL = 'http://127.0.0.1:8000'

  constructor(private client: HttpClient) { }

  getCategories(): Observable<CategoryBack[]> {
    return this.client.get<CategoryBack[]>(
      `${this.BASE_URL}/api/categories/`
    )
  }
  getSubcategoriesOfCategory(category_id: number){
    return this.client.get<SubCategoryBack[]>(
      `${this.BASE_URL}/api/categories/${category_id}/subcategories/`
    )
  }
  getProducts(category_id: number): Observable<Product[]> {
    return this.client.get<Product[]>(
      // "${this.BASE_URL}/api/categories/${category_id}/products/"
      `https://api.jsonserver.io/categories/${category_id}/products`
    )
  }


  getCategory(category_id: number): Observable<CategoryBack> {
    return this.client.get<CategoryBack>(
      `${this.BASE_URL}/api/categories/${category_id}`
    )
  }
  getSubCategory(category_id: number, subCategory_id: number): Observable<SubCategoryBack> {
    return this.client.get<SubCategoryBack>(
      `${this.BASE_URL}/api/categories/${category_id}/subcategories/${subCategory_id}`
    )
  }

}
