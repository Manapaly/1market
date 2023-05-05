import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {Order, Product, SubCategoryBack} from "../../models";
@Injectable({
  providedIn: 'root'
})
export class ProductService {
  BASE_URL = "http://127.0.0.1:8000/api";

  constructor(private client: HttpClient) { }


  getCategoryProducts(catid: number): Observable<Product[]> {
    return this.client.get<Product[]> (
      `${this.BASE_URL}/categories/${catid}/products/`
    )
  }
  // path('categories/<int:category_id>/products/',
  // ProductViewSet.as_view({'get': 'get_category_products'}), name='list of category products'),


  getCategorySubcategories(catid: number): Observable<SubCategoryBack[]> {
    return this.client.get<SubCategoryBack[]> (
      `${this.BASE_URL}/categories/${catid}/subcategories/`
    )
  }
  // path('categories/<int:category_id>/subcategories/',
  // SubCategoryViewSet.as_view({'get': 'get_subcategories_of_category'})),




  getProductsMinRate(minRate: number): Observable<Product[]> {
    return this.client.get<Product[]> (
      `${this.BASE_URL}/products/rating/${minRate}/`
    )
  }
  // path('products/rating/<int:min>/',
  // ProductViewSet.as_view({'get': 'get_products_min_rating'}), name='products with minimum rate'),



  putRatingToProduct(productID: number, minRate: number): Observable<number> {
    return this.client.get<number> (
      `${this.BASE_URL}/products/${productID}/put_rating/${minRate}/`
    )
  }
  // path('products/<int:product_id>/put_rating/<int:new_rating>/',
  // ProductViewSet.as_view({'get': 'put_rating_to_product'}), name='rate product'),



  // getProductImages(product_id: number): Observable<ProductImages[]> {
  //   return this.client.get<ProductImages[]> (
  //     `${this.BASE_URL}/products/<int:product_id>/product_images/`
  //   )
  // }
  // path('products/<int:product_id>/product_images/',
  // ProductImageViewSet.as_view({'get': 'product_images_of_product'}), name='product images of product'),


  getGeneralAllPopularProducts(): Observable<Product[]> {
    return this.client.get<Product[]> (
      `${this.BASE_URL}/popular_products/`
    )
  }
  // path('popular_products/',
  // ProductViewSet.as_view({'get': 'get_popular_products'}), name='sorted in desc by rating'),


  getProductBySearching(query: string): Observable<Product[]> {
    return this.client.get<Product[]> (
      `${this.BASE_URL}/products/searching/${query}/`
    )
  }
  // path('products/searching/<str:query>/',
  // ProductViewSet.as_view({'get': 'searching'}), name='search product'),



  getMinPriceProduct(product_id: number): Observable<Product> {
    return this.client.get<Product> (
      `${this.BASE_URL}/products/${product_id}/min_price/`
    )
  }
  // path('products/<int:product_id>/min_price/',
  // ProductViewSet.as_view({'get': 'get_min_price_product'}), name='get_min_price_product'),


  getMaxPriceProduct(product_id: number): Observable<Product> {
    return this.client.get<Product> (
      `${this.BASE_URL}/products/${product_id}/max_price/`
    )
  }
  // path('products/<int:product_id>/max_price/',
  // ProductViewSet.as_view({'get': 'get_max_price_product'}), name='get_max_price_product'),


  getCategoryProductsRatingPrice(
    category_id: number,
    min_rating: number,
    min_price: number,
    max_price: number): Observable<Product[]> {
    return this.client.get<Product[]> (
      `${this.BASE_URL}/products/categories/${category_id}/rating/${min_rating}/price/${min_price}/${max_price}/`
    )
  }
  // path('products/categories/<int:category_id>/rating/<int:min_rating>/price/<int:min_price>/<int:max_price>/',
  // ProductViewSet.as_view({'get': 'get_category_products_rating_price'}),
  // name='get category products by rating and price'),


  getSubcategoryProductsRatingPrice(
    subcategory_id: number,
    min_rating: number,
    min_price: number,
    max_price: number): Observable<Product[]> {
    return this.client.get<Product[]> (
      `${this.BASE_URL}/products/subcategories/${subcategory_id}/rating/${min_rating}/price/${min_price}/${max_price}/`
    )
  }
  // path('products/subcategories/<int:subcategory_id>/rating/<int:min_rating>/price/<int:min_price>/<int:max_price>/',
  // ProductViewSet.as_view({'get': 'get_subcategory_products_rating_price'}),
  // name='get subcategory products by rating and price'),



  getSubcategoryProducts(subcategory_id: number): Observable<Product[]> {
    return this.client.get<Product[]> (
      `${this.BASE_URL}/products/subcategories/${subcategory_id}/`
    )
  }
  // path('products/subcategories/<int:subcategory_id>/',
  // ProductViewSet.as_view({'get': 'get_subcategory_products'}),
  // name='get subcategory products '),

}
