# Copyright (c) 2021, Wahni Green Technologies and contributors
# For license information, please see license.txt

import frappe


def execute():
	frappe.rename_doc("DocType", "KSA VAT Purchase Account", "KSA VAT Details", force=True)
	frappe.reload_doc('regional', 'doctype', 'ksa_vat_details')
	frappe.reload_doc('regional', 'doctype', 'ksa_vat_setting')
	
	purchase_settings = frappe.get_all("KSA VAT Purchase Account", fields=["parent", "title", "account"])
	for d in purchase_settings:
		doc = frappe.get_doc('KSA VAT Setting', d.parent)
		doc.append("ksa_vat_purchase_accounts", {'title': d.title, 'account': d.account})
		doc.save()
	
	frappe.delete_doc('DocType', 'KSA VAT Purchase Account', ignore_missing=True)
